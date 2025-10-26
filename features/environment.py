from behave import fixture, use_fixture
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def before_all(context):
    """Executado uma vez antes de todos os testes."""
    logger.info("Iniciando execução dos testes")
    context.config.setup_logging()

def after_all(context):
    """Executado uma vez depois de todos os testes."""
    logger.info("Finalizando execução dos testes")

def before_feature(context, feature):
    """Executado antes de cada feature."""
    logger.info(f"Iniciando feature: {feature.name}")

def after_feature(context, feature):
    """Executado depois de cada feature."""
    logger.info(f"Finalizando feature: {feature.name}")

def before_scenario(context, scenario):
    """Executado antes de cada cenário."""
    logger.info(f"Iniciando cenário: {scenario.name}")

def after_scenario(context, scenario):
    """Executado depois de cada cenário."""
    logger.info(f"Finalizando cenário: {scenario.name}")
    # Limpa o contexto após cada cenário para evitar interferência
    if hasattr(context, 'result'):
        delattr(context, 'result')
    if hasattr(context, 'form_data'):
        delattr(context, 'form_data')