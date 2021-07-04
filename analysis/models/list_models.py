from edc_base.model_mixins import BaseUuidModel, ListModelMixin


class LearnVaccine(ListModelMixin, BaseUuidModel):
    pass


class Role(ListModelMixin, BaseUuidModel):
    pass

class Assets(ListModelMixin, BaseUuidModel):
    pass