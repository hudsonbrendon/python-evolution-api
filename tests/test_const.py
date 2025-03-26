from evolutionapi.const import INSTANCE_PATHS


class TestConst:
    def test_instance_paths_exists(self):
        """Test that INSTANCE_PATHS dictionary exists."""
        assert isinstance(INSTANCE_PATHS, dict)

    def test_instance_paths_create_key(self):
        """Test that INSTANCE_PATHS contains 'create' key with correct value."""
        assert "create" in INSTANCE_PATHS
        assert INSTANCE_PATHS["create"] == "/instance/create"
