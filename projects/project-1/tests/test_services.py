from src.services.compliance_service import analyze_text

def test_analyze_text_basic():
    result = analyze_text("Investir no produto XPTO com risco")

    assert isinstance(result, dict)
    assert "is_compliant" in result
    assert "reason" in result
    assert "mentioned_products" in result


def test_analyze_text_detect_product():
    result = analyze_text("Produto XPTO")

    assert isinstance(result["mentioned_products"], list)