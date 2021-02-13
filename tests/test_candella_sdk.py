from candella_sdk import __version__, sdk


def test_version():
    assert __version__ == '1.0.0-alpha1'


def test_validation_fails_on_empty():
    """Test that the SDK validation fails on an empty app."""
    validated, reason = sdk.validate("examples/Empty.aosapp")
    assert not validated and reason == "missing manifest.json file"


def test_validation_fails_on_invalid_keys():
    """Test that the SDK validation fails with invalid keys."""
    validated, reason = sdk.validate("examples/InvalidManifestKey.aosapp")
    assert not validated and reason.startswith("invalid manifest key: ")


def test_validation_fails_on_missing_required_keys():
    """Test that the SDK validation fails when a required key is missing."""
    validated, reason = sdk.validate("examples/MissingRequired.aosapp")
    assert not validated and reason.startswith("missing required key: ")


def test_validation_fails_on_missing_icons():
    """Test that the SDK validation fails when the iconset is missing."""
    validated, reason = sdk.validate("examples/MissingIconset.aosapp")
    assert not validated and reason == "missing iconset folder"


def test_validation_succeeds_on_valid_apps():
    """Test that the SDK validates and app successfully."""
    validated, _ = sdk.validate("examples/Valid.aosapp")
    assert validated
