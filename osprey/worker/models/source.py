import requests, datetime

from sqlalchemy.orm                import relationship
from sqlalchemy                    import Column, Integer, String
from osprey.worker.models.database import Base, Session
# from osprey.worker.jobs.verifier   import verifier_microservice
from osprey.worker.lib.serializer  import encode

from osprey.worker.models.source_version import SourceVersion
from osprey.worker.models.source_file    import SourceFile

# Assume that this is sa read-only class
class Source(Base):
    __tablename__ = 'source'
    __table_args__ = {'extend_existing': True}
    id            = Column(Integer, primary_key=True)
    name          = Column(String)
    url           = Column(String)
    description   = Column(String)
    timer         = Column(Integer) # in seconds
    verifier      = Column(String)
    modifier      = Column(String)
    user_endpoint = Column(String)
    timer_job_id  = Column(String)
    flow_kind     = Column(Integer)
    versions      = relationship("SourceVersion", back_populates="source", lazy=False)

    def __repr__(self):
        return f"Source(id={self.id}, name={self.name}, url={self.url}, timer={self.timer_readable()})"

    def add_new_version(self, new_data, format):
        with Session() as session:
            version_number = self.last_version() + 1
            new_version             = SourceVersion(version=version_number, source_id= self.id)
            new_version.source_file = SourceFile(encoding='utf-8',
                                                 file_type=format,
                                                 args={
                                                     'file': new_data,
                                                     'version': version_number,
                                                     'source_id': self.id
                                                     })
            session.add(new_version)
            session.commit()

    def download(self):
        """ 
            NOTE: Maybe in CSV or get format from user.

            But assuming that it is gonna be in JSON for now
        """
        data = requests.get(self.url)
        # TODO: Change this to automatically pick
        return data.content.decode('utf-8'), 'csv'

    def last_version(self):
        try:
            l_version = self.versions[len(self.versions) - 1]
            return l_version.version
        except IndexError:
            return 0

    def timer_readable(self):
        if not(self.timer):
            return None

        return str(datetime.timedelta(seconds=self.timer))
    
    @classmethod
    def get(cls, source_id):
        with Session() as session:
            source = session.query(Source).get(source_id)
        return source

    # @classmethod
    # def nearest_refresh(cls):       # Assume that it runs every 5 mins
    #     with Session() as s:
    #         return s.query(cls).count()

"""

NOTE: This class is duplicated from the `class Source` from

    /osprey/server/models/source.py

But the usecase is, to seperates the representation for different microservices

"""
