from models.custom_deployment import CustomDeployment


class Nginx(CustomDeployment):

  def __init__(self, name: str, image: str, labels: list, match_labels: list):
    super().__init__(name, image, labels, match_labels)

  @property
  def name(self) -> str:
    return super().name
  
  @property
  def image(self) -> str:
    return super().image

  @property
  def labels(self) -> list:
    return super().labels

  @property
  def match_labels(self) -> list:
      return super().match_labels
  
  @property
  def replicas(self) -> int:
      return super().replicas

  def build(self, env):
    super().build()
    if env == 'local': # inherited python setters are busted
      super(Nginx, type(self)).replicas.fset(self, 1)
    elif env == 'dev':
      super(Nginx, type(self)).replicas.fset(self, 3)
    elif env == 'prod':
      super(Nginx, type(self)).replicas.fset(self, 5)
