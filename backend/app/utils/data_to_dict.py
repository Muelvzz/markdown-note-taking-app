def data_to_dict(object):
  return {c.name: getattr(object, c.name) for c in object.__table__.columns}