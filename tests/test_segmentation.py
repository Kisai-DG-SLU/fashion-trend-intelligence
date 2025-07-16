# tests/test_segmentation.py

from fashion_trend_intelligence.segmentation import main

def test_segmentation_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "Segmentation placeholder" in captured.out
