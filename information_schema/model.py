import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = 'util.lab'
PORT = '3306'
DATABASE = 'information_schema'
DBUSER = 'admin'
DBPASS = 'info_Schema'
ECHO = False
VERBOSE = False
ENCODING = 'UTF-8'
DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'.format(user=DBUSER,
                                                                                          password=DBPASS,
                                                                                          host=HOST,
                                                                                          port=PORT,
                                                                                          database=DATABASE)
engine = sqlalchemy.create_engine(DATABASE_URI,
                                  encoding=ENCODING,
                                  echo=ECHO,
                                  echo_pool=VERBOSE)

Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine, info={})

class CharacterSet(Base):
    __table__ = sqlalchemy.Table('CHARACTER_SETS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key':[__table__.columns.CHARACTER_SET_NAME]
    }

class Collation(Base):
    __table__ = sqlalchemy.Table('COLLATIONS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.COLLATION_NAME]
    }

class CollationCharacterSetApplicability(Base):
    __table__ = sqlalchemy.Table('COLLATION_CHARACTER_SET_APPLICABILITY', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.COLLATION_NAME,
                        __table__.columns.CHARACTER_SET_NAME]
    }

class Column(Base):
    __table__ = sqlalchemy.Table('COLUMNS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.COLUMN_NAME]
    }

class ColumnPrivileges(Base):
    __table__ = sqlalchemy.Table('COLUMN_PRIVILEGES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.COLUMN_NAME,
                        __table__.columns.PRIVILEGE_TYPE,
                        __table__.columns.GRANTEE]
    }

class Engine(Base):
    __table__ = sqlalchemy.Table('ENGINES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.ENGINE]
    }

class Event(Base):
    __table__ = sqlalchemy.Table('EVENTS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.EVENT_NAME,
                        __table__.columns.EVENT_SCHEMA]
    }

class File(Base):
    __table__ = sqlalchemy.Table('FILES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.FILE_ID]
    }

class GlobalStatus(Base):
    __table__ = sqlalchemy.Table('GLOBAL_STATUS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.VARIABLE_NAME]
    }

class GlobalVariable(Base):
    __table__ = sqlalchemy.Table('GLOBAL_VARIABLES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.VARIABLE_NAME]
    }

class KeyColumnUsage(Base):
    __table__ = sqlalchemy.Table('KEY_COLUMN_USAGE', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.TABLE_NAME,
                        __table__.columns.COLUMN_NAME,
                        __table__.columns.ORDINAL_POSITION]
    }

class Parameter(Base):
    __table__ = sqlalchemy.Table('PARAMETERS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.PARAMETER_NAME]
    }

class Partition(Base):
    __table__ = sqlalchemy.Table('PARTITIONS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.TABLE_SCHEMA,
                        __table__.columns.TABLE_NAME]
    }

class Plugins(Base):
    __table__ = sqlalchemy.Table('PLUGINS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.PLUGIN_NAME]
    }

class Process(Base):
    __table__ = sqlalchemy.Table('PROCESSLIST', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.ID]
    }

class Profile(Base):
    __table__ = sqlalchemy.Table('PROFILING', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.QUERY_ID]
    }

class ReferentialConstraint(Base):
    __table__ = sqlalchemy.Table('REFERENTIAL_CONSTRAINTS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.CONSTRAINT_SCHEMA,
                        __table__.columns.CONSTRAINT_NAME]
    }

class Routine(Base):
    __table__ = sqlalchemy.Table('ROUTINES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.ROUTINE_SCHEMA,
                        __table__.columns.ROUTINE_NAME]
    }

class Schema(Base):
    __table__ = sqlalchemy.Table('SCHEMATA', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.SCHEMA_NAME]
    }

class SchemaPrivilege(Base):
    __table__ = sqlalchemy.Table('SCHEMA_PRIVILEGES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.GRANTEE,
                        __table__.columns.TABLE_SCHEMA,
                        __table__.columns.PRIVILEGE_TYPE]
    }

class SessionStatus(Base):
    __table__ = sqlalchemy.Table('SESSION_STATUS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.VARIABLE_NAME]
    }

class SessionVariable(Base):
    __table__ = sqlalchemy.Table('SESSION_VARIABLES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.VARIABLE_NAME]
    }

class Statistic(Base):
    __table__ = sqlalchemy.Table('STATISTICS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.COLUMN_NAME,
                        __table__.columns.INDEX_NAME]
    }

class Table(Base):
    __table__ = sqlalchemy.Table('TABLES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.TABLE_SCHEMA,
                        __table__.columns.TABLE_NAME]
    }

class Tablespace(Base):
    __table__ = sqlalchemy.Table('TABLESPACES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.TABLESPACE_NAME]
    }

class TableConstraint(Base):
    __table__ = sqlalchemy.Table('TABLE_CONSTRAINTS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.TABLE_SCHEMA,
                        __table__.columns.TABLE_NAME,
                        __table__.columns.CONSTRAINT_NAME]
    }

class TablePrivilege(Base):
    __table__ = sqlalchemy.Table('TABLE_PRIVILEGES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.TABLE_SCHEMA,
                        __table__.columns.TABLE_NAME,
                        __table__.columns.PRIVILEGE_TYPE,
                        __table__.columns.GRANTEE]
    }

class Trigger(Base):
    __table__ = sqlalchemy.Table('TRIGGERS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.TRIGGER_SCHEMA,
                        __table__.columns.TRIGGER_NAME]
    }

class UserPrivilege(Base):
    __table__ = sqlalchemy.Table('USER_PRIVILEGES', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.GRANTEE,
                        __table__.columns.TABLE_CATALOG,
                        __table__.columns.PRIVILEGE_TYPE]
    }

class View(Base):
    __table__ = sqlalchemy.Table('VIEWS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.TABLE_SCHEMA,
                        __table__.columns.TABLE_NAME]
    }

class InnodbBufferPage(Base):
    __table__ = sqlalchemy.Table('INNODB_BUFFER_PAGE', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.POOL_ID,
                        __table__.columns.BLOCK_ID]
    }
class InnodbTransaction(Base):
    __table__ = sqlalchemy.Table('INNODB_TRX', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.trx_id]
    }

class InnodbBufferPoolStatistic(Base):
    __table__ = sqlalchemy.Table('INNODB_BUFFER_POOL_STATS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.POOL_ID]
    }

class InnodbLockWait(Base):
    __table__ = sqlalchemy.Table('INNODB_LOCK_WAITS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.requested_lock_id]
    }

class InnodbLock(Base):
    __table__ = sqlalchemy.Table('INNODB_LOCKS', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.lock_id,
                        __table__.columns.lock_trx_id] # TODO : is this needed? are lock IDs reused?
    }

class InnodbBufferPageLRU(Base):
    __table__ = sqlalchemy.Table('INNODB_BUFFER_PAGE_LRU', Base.metadata, autoload=True)
    __mapper_args__ = {
        'primary_key': [__table__.columns.POOL_ID,
                        __table__.columns.LRU_POSITION]
    }
