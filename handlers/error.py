from utils.logger import logger



async def global_error(
    update,
    context
):

    logger.error(
        context.error
    )
