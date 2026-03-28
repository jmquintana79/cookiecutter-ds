# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-03-28 18:10:41
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-03-28 18:27:10

import pytest

from helpers import create_project_structure


@pytest.fixture
def project_dir(tmp_path):
    """Directorio temporal con la estructura completa del proyecto."""
    create_project_structure(tmp_path)
    return tmp_path