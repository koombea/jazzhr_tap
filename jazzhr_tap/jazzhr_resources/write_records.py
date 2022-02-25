import singer

def main(stream, schema, key_properties, read_record, records):
  singer.write_schema(
      stream_name=stream,
      schema=schema,
      key_properties=key_properties)
  for record in records:
    singer.write_record(stream_name=stream,
                          record=read_record(record))