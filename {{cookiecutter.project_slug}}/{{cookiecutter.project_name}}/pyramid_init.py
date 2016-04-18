import logging

from baseplate import make_metrics_client, config, Baseplate
from baseplate.integration.pyramid import BaseplateConfigurator
from pyramid.config import Configurator


logger = logging.getLogger(__name__)


class {{ cookiecutter.service_name }}(object):
    def __init__(self):
        pass

    def is_healthy(self, request):
        return {
            "status": "healthy",
        }

    # TODO: build your service here



def make_wsgi_app(app_config):
    cfg = config.parse_config(app_config, {
        # TODO: add your config spec here
    })

    metrics_client = make_metrics_client(app_config)

    baseplate = Baseplate()
    baseplate.configure_logging()
    baseplate.configure_metrics(metrics_client)

    configurator = Configurator(settings=app_config)

    baseplate_configurator = BaseplateConfigurator(baseplate)
    configurator.include(baseplate_configurator.includeme)

    controller = {{ cookiecutter.service_name }}()
    configurator.add_route("health", "/health", request_method="GET")
    configurator.add_view(
        controller.is_healthy, route_name="health", renderer="json")

    # TODO: add more routes and views here

    return configurator.make_wsgi_app()

