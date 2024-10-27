import ast
import importlib
import logging
import pathlib
import sys


from typing import Tuple


import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()

sys.path.insert(0, str(proj_folder))

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)


@pytest.fixture
def ast_tree(py_file:pathlib.Path) -> ast.AST:
    code = py_file.read_text(encoding="utf-8")
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        pytest.fail(f"Syntax error in file: {py_file.relative_to(proj_folder)}\n{e}")
    return tree


@pytest.fixture
def rel_path(py_file:pathlib.Path) -> pathlib.Path:
    return py_file.relative_to(proj_folder)


def test_syntax_validity(ast_tree:ast.AST):
    assert ast_tree is not None


@pytest.fixture(scope="session")  # Session scope to share the allowed modules across tests
def allowed_modules() -> Tuple[str]:
    return tuple('pathlib',)


def test_allowed_imports(rel_path:pathlib.Path, ast_tree:ast.AST, allowed_modules:Tuple[str]):
    for node in ast.walk(ast_tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            module_name = node.module if isinstance(node, ast.ImportFrom) else node.names[0].name
            if module_name not in allowed_modules:
                pytest.fail(
                    f"Import of disallowed module '{module_name}' in {rel_path}\n"
                    f"{rel_path} 파일에서 '{module_name}' 모듈을 import 않기 바랍니다."
                )


def test_importable(py_file:pathlib.Path):
    m = importlib.import_module(py_file.name.split(".")[0])
    assert m is not None


@pytest.mark.parametrize("prohibited_function", ["input", "map", "sum"])
def test_no_prohibited_functions(rel_path:pathlib.Path, ast_tree:ast.AST, prohibited_function:str):
    """Checks that the exercise.py file does not use prohibited functions."""
    for node in ast.walk(ast_tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == prohibited_function
        ):
            pytest.fail(
                f"Use of '{prohibited_function}()' function is prohibited in {rel_path}.\n"
                f"{rel_path} 파일에서 '{prohibited_function}()' 함수를 사용하지 마십시오."
            )


if __name__ == "__main__":
    pytest.main([__file__])
