# package_sharing_app

Here is an example of how the [greetings_package](https://github.com/carlosgomez2/greetings_package) package could be consumed from the file system in a basic flask app. You need to follow steps from README in greetings_package to build the package and then you need to change the filepath `requirements.txt` in this app

```txt
Flask==3.0.0
file:///your-full-path/greetings_package/dist/greetings_package-0.1.tar.gz
```
