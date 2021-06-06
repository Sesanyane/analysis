from datetime import datetime
from dateutil.tz import gettz

from django.apps import AppConfig

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfigs


class AnalysisConfig(AppConfig):
    name = 'analysis'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Botswana Red Cross'
    institution = 'Africort Investments'


class EdcProtocolAppConfig(BaseEdcProtocolAppConfigs):
        protocol = 'Botswana Red Cross'
        protocol_name = 'Botswana Red Cross'
        protocol_number = '012'
        protocol_title = ''
        study_open_datetime = datetime(
            2021, 4, 15, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))