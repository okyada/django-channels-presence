from django import dispatch

# Provides the arguments `"room"`, `"added"`, `"removed"`, and
# `"bulk_change"` to listeners (specified by the `providing_args`
# argument to `Signal` prior to Django 4.0).
presence_changed = dispatch.Signal()
