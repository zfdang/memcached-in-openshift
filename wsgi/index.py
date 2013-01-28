# -*- coding: UTF-8 -*-
from flask import Blueprint, render_template, current_app

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    message = ""
    stats = current_app.config['cache'].get_stats()
    for stat in stats:
        message += "Server IP: %s\n" % (stat[0])
        message += "Stats:\n"
        infodict = stat[1]
        keys = infodict.keys()
        keys.sort()
        for key in keys:
            message += "    %s = %s\n" % (key, infodict[key])
    # stats = "\n".join(stats)
    return render_template('index.html', serverinfo=message)
