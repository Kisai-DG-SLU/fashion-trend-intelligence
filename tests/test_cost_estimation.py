# tests/test_cost_estimator.py

from fashion_trend_intelligence.cost_estimator import main

def test_cost_estimator_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "Cost estimator placeholder" in captured.out
