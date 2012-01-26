#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'


################################################################################
"""

Lot of files generated by the collective.generic packages  will try to load user defined objects in user specific files.
The final goal is to regenerate easyly the test infrastructure on templates updates without impacting
user-specific test boilerplate.
We do not use paster local commands (insert/update) as it cannot determine witch is specific or not and we prefer to totally
separe generated stuff and what is user specific



If you need to edit something in this file, you must have better to do it in:


    - user_globals.py

All from there will be imported in this namespace

"""
################################################################################


# try to load testing product globals
try: from collective.testing.tests.globals import *
except Exception, e: pass
try:from collective.externalimageeditor import app_config
except:pass


# try to import, but not fail as we can do without (for example in a thirdparty which adapt the testcase)
try: from collective.externalimageeditor.app_config import GLOBALS
except:pass
try: from collective.externalimageeditor.app_config import PRODUCT_DEPENDENCIES
except:pass
try: from collective.externalimageeditor.app_config import SKIN
except:pass
try:from collective.externalimageeditor.tests_tools import getWorkflows
except:pass
try:from five.grok.testing import grok as fgrok
except:pass
try:
    from Products.Five.testbrowser import Browser
    FF2_USERAGENT =  'Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14'
    GENTOO_FF_UA = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.3) Gecko/20090912 Gentoo Shiretoko/3.5.3'
    class Browser(Browser):
        """Patch the browser class to be a little more like a webbrowser."""

        def __init__(self, url=None, mech_browser=None):
            Browser.__init__(self, url, mech_browser)
            self.mech_browser.set_handle_robots(False)
            self.mech_browser.addheaders = [('User-agent' , GENTOO_FF_UA)]
            if url is not None:
                self.open(url) 

    browser = Browser()
except:pass
try:from Products.statusmessages.interfaces import IStatusMessage
except:pass
try:from Acquisition import aq_inner, aq_parent, aq_self
except:pass
try:from Acquisition import aq_explicit
except:pass
try:from five import grok
except:pass
try:import collective
except:pass
try:from Products.CMFCore.utils import getToolByName
except:pass

try:
    import zope
    from zope.traversing.adapters import DefaultTraversable
    zope.component.provideAdapter(DefaultTraversable, [None])
    class Request(zope.publisher.browser.TestRequest):
        def __setitem__(self, name, value):
            self._environ[name] = value
    # alias
    TestRequest = Request
    def make_request(url='http://nohost/@@myview',form=None, *args,  **kwargs):
        r = Request(environ = {'SERVER_URL': url, 'ACTUAL_URL': url}, form=form, *args, **kwargs)
        zope.interface.alsoProvides(r, zope.annotation.interfaces.IAttributeAnnotatable)
        return r
except Exception, e:pass

ZOPETESTCASE = (('ZOPE_TESTCASE' in os.environ) or ('ZOPETESTCASE' in os.environ))
DEFAULT_CONFIG_FILE = os.path.join(
    os.path.dirname(__file__), 'testing.cfg'
)

# if you have plone.reload out there add an helper to use in doctests while programming
# just use preload(module) in pdb :)
# it would be neccessary for you to precise each module to reload, this method is also not recursive.
# eg: (pdb) from foo import bar;preload(bar)
try:
    def preload(modules_or_module, excludelist=None):
        modules = modules_or_module
        if not (isinstance(modules_or_module, list)
                or isinstance(modules_or_module, tuple)):
            modules = [modules_or_module]
        if not excludelist:
            excludelist = []
        import sys
        if not modules:
            modules = sys.modules
        from plone.reload.xreload import Reloader
        print modules
        for module in modules:
            if not module in excludelist:
                try:
                    Reloader(module).reload()
                except Exception, e:
                    pass
except:
    pass
UNTESTED_WARNING = """
*****************************   WARNING   ************************************
*
* * you are testing with FAILS_ON_UNTESTED_ELEMENT setted to False
* *
* * The only exception to do this is : catch all untested element on one shot !
* *
* ******************************************************************************
*
* """

def format_test_title(title):
    sep = '*' * (len(title)+4)
    return "\n%s\n %s \n%s\n" % (sep, title, sep)

# load user specific globals
try: from collective.externalimageeditor.tests.user_globals import *
except: pass

def print_contents(browser, dest='~/.browser.html'):
    """Print the browser contents somewhere for you to see its context
    in doctest pdb, type print_contents(browser) and that's it, open firefox
    with file://~/browser.html."""
    import os
    open(os.path.expanduser(dest), 'w').write(browser.contents)

# vim:set et sts=4 ts=4 tw=80:
