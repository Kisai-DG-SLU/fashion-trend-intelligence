# tests/test_visualization.py

from fashion_trend_intelligence.visualization import main

def test_visualization_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "Visualization placeholder" in captured.out
