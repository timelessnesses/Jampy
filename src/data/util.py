import aiofiles
async def open(*args,**kwargs):
    a = await aiofiles.open(*args,**kwargs)
    return a