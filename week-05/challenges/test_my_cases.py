"""W5 综合题 A：本人另选的一组输入与预期。

实现通过 challenges/conftest.py 的同名 fixture 传入，不直接导入参考实现，
因此 --challenge-impl 仍可切换 student／reference／broken。
运行：uv run --locked pytest -q challenges -k summarize --challenge-impl=student
"""


def test_my_summarize_case(summarize_values):
    values = [4, -1, 4, 2, -1, 0, 2, 4]
    before = values.copy()

    result = summarize_values(values)

    assert result == {
        "unique": [4, -1, 2, 0],
        "counts": {4: 3, -1: 2, 2: 2, 0: 1},
        "repeated": {4, -1, 2},
    }
    # len(values) == 8，频数合计应与输入长度一致
    assert sum(result["counts"].values()) == 8
    # 0 只出现一次，不能进入 repeated；首次顺序不是排序，也不是 set 顺序
    assert 0 not in result["repeated"]
    assert result["unique"] != sorted(set(values))
    # 原输入保持不变
    assert values == before


def test_my_summarize_case_is_reusable(summarize_values):
    values = [4, -1, 4, 2, -1, 0, 2, 4]
    before = values.copy()

    first = summarize_values(values)
    second = summarize_values(values)

    assert first is not second
    assert first["unique"] is not second["unique"]
    assert first["counts"] is not second["counts"]
    assert first["repeated"] is not second["repeated"]

    first["unique"].append(99)
    first["counts"][99] = 2
    first["repeated"].add(99)

    assert 99 not in second["unique"]
    assert 99 not in second["counts"]
    assert 99 not in second["repeated"]
    assert values == before
