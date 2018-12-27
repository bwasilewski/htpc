# HTPC

Since 2015, I have been maintaining a home media server that runs Linux Mint. It meant to serve a few purposes:

* Store and serve media files across my home network
* Backup important data
* Learn a bit about servers and networking
* Provide a chance to use Linux for the first time

The goal of this project is to create a dashboard that will display data such as available disk space by employing different available APIs.

## Getting Started

```
$ source htpc_env/bin/activate  # activate the virtual environment
$ python main.py                # start the application
```

View the application at [http://127.0.0.1:5000](http://127.0.0.1:5000)


## Goals

* Show disk usage across all disks
* Warn if a disk is low on space
* Show current plex/kodi activity
* Recently downloaded items
* Suggested movies/tv shows
* Remote control the TV via mobile devices
* Drive health?