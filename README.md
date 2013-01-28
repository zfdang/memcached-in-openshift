Flask + Memcached on OpenShift
==================

This git repository helps you get up and running quickly w/ a Flask + Memcached installation on OpenShift.


Running on OpenShift
----------------------------

Create an account at http://openshift.redhat.com/

Create a python-2.6 application

    rhc app create -a memcached -t python-2.6

Add this upstream memcached repo

    cd memcached
    git remote add upstream -m master git://github.com/zfdang/memcached-in-openshift.git
    git pull -s recursive -X theirs upstream master
    
Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://memcached-$yournamespace.rhcloud.com

