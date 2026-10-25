"""Meaningful gates for live-test setup and failed/incomplete model runs."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('eval_runner', Path(__file__).resolve().parents[1] / 'evals/run.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class EvaluationGateTests(unittest.TestCase):
    def test_trigger_with_timeout_is_not_a_successful_run(self):
        self.assertEqual(runner.evaluation_exit_status([{'triggered': True, 'auto_pass': False, 'failures': ['run_error']}]), 1)

    def test_artifact_violation_or_incomplete_result_fails(self):
        self.assertEqual(runner.evaluation_exit_status([{'auto_pass': True}, {'auto_pass': False}]), 1)
        self.assertEqual(runner.evaluation_exit_status([{}]), 1)
        self.assertEqual(runner.evaluation_exit_status([]), 1)

    def test_only_completed_successful_checks_pass(self):
        self.assertEqual(runner.evaluation_exit_status([{'auto_pass': True}, {'auto_pass': True}]), 0)

    def test_no_silent_fallback_to_personal_configuration(self):
        with self.assertRaises(ValueError):
            runner.validate_test_config(None)
        with self.assertRaises(ValueError):
            runner.validate_test_config(str(Path.home() / '.qoder'))

    def test_separate_existing_profile_is_accepted_without_reading_its_contents(self):
        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual(runner.validate_test_config(temp), Path(temp).resolve())


if __name__ == '__main__':
    unittest.main()
