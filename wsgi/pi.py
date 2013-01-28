# -*- coding: UTF-8 -*-
from flask import Blueprint, render_template
from pi_chudnovsky_bs import pi_chudnovsky_bs
from decorators import cached


bp = Blueprint('pi', __name__)


@bp.route("/", defaults={'digits': 20000})
@bp.route("/<int:digits>/")
@cached(180)
def index(digits):
    pi = pi_chudnovsky_bs(digits)
    return render_template("pi.html", pi=pi, digits=digits)
