# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
        
        def test_fail():
            assert 1 == 2
    """)
    return testdir


def test_with_honey(sample_test):
    result = sample_test.runpytest("--honey")

    result.stdout.fnmatch_lines(["*.HONEY*", ])
    assert result.ret == 1


def test_honey_with_verbose(sample_test):
    result = sample_test.runpytest("-v", "--honey")

    result.stdout.fnmatch_lines(["*::test_fail *HONEY for bread.*", ])
    assert result.ret == 1

def test_not_honey_verbose(sample_test):
    result = sample_test.runpytest("-v")

    result.stdout.fnmatch_lines(["*::test_fail *FAILED*", ])    
    assert result.ret == 1


def test_header(sample_test):
    result = sample_test.runpytest("--honey")

    result.stdout.fnmatch_lines(["*Thank you for using honey.", ])


def test_header_not_honey(sample_test):
    result = sample_test.runpytest()
    thanks_message = "*Thank you for using honey."

    assert thanks_message not in result.stdout.lines


def test_help_message(testdir):
    result = testdir.runpytest("--help")

    result.stdout.fnmatch_lines([
        "honey:",
        "*--honey*honey: turn FAILED into HONEY for bread.",
    ])

