# coding=utf-8
from __future__ import with_statement
import os
import yaml

from clint.textui import puts, indent, colored

from hazel.utils import ObjectDict, path_to_file, force_mkdir, g


def load_config():
    with open('config.yml', 'r') as f:
        g.config = yaml.load(f.read())


def load_template_config():
    with open(path_to_file(g.template,'config.yml'), 'r') as f:
        g.template_config = yaml.load(f.read())


def load_path():
    g.posts = 'posts'
    g.template = os.path.join('templates', g.config['template'])
    g.template_assets = os.path.join(g.template, 'assets')
    g.site = 'site'
    g.site_assets = os.path.join(g.site, 'assets')
