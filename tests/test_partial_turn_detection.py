"""Test that partial TurnDetection updates work correctly."""


from speaches.types.realtime import (
    SessionUpdateEvent,
)


class TestPartialTurnDetectionUpdate:
    """Verify partial turn_detection updates are accepted."""

    def test_partial_turn_detection_create_response_only(self) -> None:
        """session.update with only create_response should be valid."""
        event_data = {
            "type": "session.update",
            "session": {
                "turn_detection": {
                    "create_response": False,
                }
            },
        }

        # BUG: This raises ValidationError because TurnDetection requires all fields
        # After fix: should NOT raise
        event = SessionUpdateEvent.model_validate(event_data)

        assert event.session.turn_detection is not None
        assert event.session.turn_detection.create_response is False

    def test_partial_turn_detection_threshold_only(self) -> None:
        """session.update with only threshold should be valid."""
        event_data = {
            "type": "session.update",
            "session": {
                "turn_detection": {
                    "threshold": 0.8,
                }
            },
        }

        event = SessionUpdateEvent.model_validate(event_data)
        assert event.session.turn_detection.threshold == 0.8

    def test_partial_session_without_turn_detection(self) -> None:
        """session.update without turn_detection should still work."""
        event_data = {
            "type": "session.update",
            "session": {
                "modalities": ["text"],
            },
        }

        event = SessionUpdateEvent.model_validate(event_data)
        assert event.session.modalities == ["text"]
