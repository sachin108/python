'''
When your setup or teardown involves I/O that should be awaited (database connections, HTTP sessions, WebSockets), 
you need the async variant: async with. The protocol mirrors the sync version but uses __aenter__ and __aexit__ — 
both of which are coroutines ( concurrency design pattern used to simplify asynchronous code by allowing functions 
to suspend execution and resume later without blocking threads )
'''