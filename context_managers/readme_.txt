Sometimes, a program uses a given resource and doesn’t release the associated memory when it no longer needs the 
resource. This kind of issue is called a memory leak because the available memory shrinks every time you create a 
new instance of a resource without releasing the unneeded ones.

For example, say that a program that uses databases keeps creating new connections without releasing the old ones or 
reusing them. In that case, the database back end can stop accepting new connections. 

Another possibility is that your application runs into errors or exceptions that cause the control flow to bypass 
the code responsible for releasing the resource at hand. 

Python’s context managers make sure to release these resources after usage. If they are not released then it 
will lead to resource leakage and may cause system to either slow down or crash.

They provide a neat way to automatically set up and clean up resources, ensuring they’re properly managed 
even if errors occur.

use these with the with statement.

