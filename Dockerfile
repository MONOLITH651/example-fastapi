FROM python:3
# base image
WORKDIR /usr/src/app
# optional, working directory, 
# it will tell docker from where all commands running from
COPY requirements.txt ./
# copying from local machine
# ./ is directory where we want to set it up (WORKDIR./, OR /usr/src/app)
# requirements.txt is here for optimisation, since code is executed top to button
RUN pip install --no-cache-dir -r requirements.txt
# installing dependencies
# --no-cache-dir
# caches results
COPY . .
# copying everthing from source code directory into . current dir of the container (WORKDIR)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# command that we want to start when we start container
# each word is broken on command