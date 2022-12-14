import uvicorn

from . import config

if __name__ == '__main__':
    uvicorn.run(
        "src:app",
        host=config.deploy.DEPLOY_HOST,
        port=config.deploy.DEPLOY_PORT,
        debug=config.deploy.DEPLOY_DEBUG,
        reload=config.deploy.DEPLOY_RELOAD,
        access_log=config.deploy.DEPLOY_ACCESS_LOG
    )
