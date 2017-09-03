#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ims_site.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


# FIXME: proper templates to do (urls.py for subsites (delete, create, edit) does not work
# TODO: import module working with admin
# TODO: get valid superuser credentials (or create one)
# TODO: make outer js files work (not inner script - outside of html)
# FIXME: proper templates to do (
