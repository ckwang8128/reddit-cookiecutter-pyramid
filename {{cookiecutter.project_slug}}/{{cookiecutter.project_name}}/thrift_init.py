import logging

from baseplate import Baseplate, make_metrics_client, config
from baseplate.integration.thrift import BaseplateProcessorEventHandler

from .{{ cookiecutter.project_slug }}_thrift import {{ cookiecutter.service_name }}


logger = logging.getLogger(__name__)


class Handler({{ cookiecutter.service_name }}.ContextIface):
    def __init__(self):
        pass

    def is_healthy(self, context):
        # TODO: check that your service has everything it needs to to function
        return True

    # TODO: implement your service here!


def make_processor(app_config):
    cfg = config.parse_config(app_config, {
        # TODO: add your config spec here
    })

    metrics_client = make_metrics_client(app_config)

    baseplate = Baseplate()
    baseplate.configure_logging()
    baseplate.configure_metrics(metrics_client)

    handler = Handler()
    processor = {{ cookiecutter.service_name }}.ContextProcessor(handler)
    event_handler = BaseplateProcessorEventHandler(logger, baseplate)
    processor.setEventHandler(event_handler)

    return processor
