# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('honey')
    group.addoption(
        '--honey',
        action='store_true',
        help='honey: turn FAILED into HONEY for bread.'
    )

def pytest_report_header(config):
    """Thank tester for running tests."""
    if config.getoption('honey'):
        return "Thank you for using honey."

def pytest_report_teststatus(report, config):
    """Change test status to HONEY."""
    if report.when == 'call':
        if report.failed and config.getoption('honey'):
            return (report.outcome, 'HONEY', 'HONEY for bread.')
