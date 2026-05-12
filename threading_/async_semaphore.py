import asyncio


def fetch_data(url):
    pass

# This will cause problems, because no concurrency control. All 1000 requests fire simultaneously, overwhelming both 
# our system and the target API.
async def bad_scraper():
    urls = [f"https://api.example.com/data/{i}" for i in range(1000)]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)  # All 1000 requests at once!


async def good_scraper():
    sems=asyncio.Semaphore(10) # Only 10 concurrent requests

    async def controlled_fetch(url):
        async with sems:
            return await fetch_data(url)
        
    urls = [f"https://api.example.com/data/{i}" for i in range(1000)]
    tasks = [controlled_fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)  # Controlled concurrency

    '''
        Just like a bouncer at a nightclub who only lets a certain number of people in at once, a semaphore only allows a 
        specified number of coroutines to execute a particular section of code simultaneously.
    '''