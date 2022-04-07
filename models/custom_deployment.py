class CustomDeployment:
  _name: str
  _image: str
  _labels: list
  _replicas: int
  _match_labels: list

  def __init__(self, name: str, image: str, labels: list, match_labels: list):
    self._name = name
    self._image = image
    self._labels = labels
    self._match_labels = match_labels
    self._replicas = 2

  @property
  def name(self) -> str:
    return self._name

  @property
  def image(self) -> str:
    return self._image

  @property
  def labels(self) -> list:
    return self._labels

  @property
  def replicas(self) -> int:
    return self._replicas

  @replicas.setter
  def replicas(self, replicas: int):
    if replicas < 0:
      raise ValueError('replica count must be zero or positive')
    self._replicas = replicas
    

  @property
  def match_labels(self) -> list:
    return self._match_labels

  def build(self):
    # default build function
    # this contains basic build functionality across all deployments
    # could be called by super() or overloaded by default
    print('default build function')
