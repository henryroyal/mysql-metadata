import click
import json
from datetime import datetime
import information_schema.model as model

TABLE_TO_INSPECT = 'mysql'
session = model.Session()


def serialize_table(table):
    table_hash = table.__dict__
    copy = {}

    for k, v in table_hash.items():

        if k == '_sa_instance_state':
            # skip sqlalchemy internal state
            continue

        if type(v) == datetime:
            v = datetime.strftime(v, '%e')

        copy[k] = str(v)

    return copy


def main():

    all_tables = session.query(model.Table).filter(model.Table.TABLE_SCHEMA == TABLE_TO_INSPECT).all()

    for table in all_tables:
        serialized_table_table = serialize_table(table)
        click.secho(fg='red',
                    text=json.dumps(serialized_table_table)
        )

    all_columns = session.query(model.Column).filter(model.Column.TABLE_SCHEMA == TABLE_TO_INSPECT).all()

    for column in all_columns:
        serialized_column_table = serialize_table(column)
        click.secho(fg='white',
                    text=json.dumps(serialized_column_table)
        )

    all_database_processes = session.query(model.Process).all()

    for process in all_database_processes:
        serialized_process_table = serialize_table(process)
        click.secho(fg='blue',
                    text=json.dumps(serialized_process_table)
        )


if __name__ == '__main__':
    main()
