import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_repo", ROOT / "tooling" / "validate_repo.py"
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VALIDATOR)


class CatalogMaturityTest(unittest.TestCase):
    def validate(
        self,
        status: str,
        forward_tested: bool | None,
        structure: bool = True,
        eval_spec: bool = True,
    ) -> list[str]:
        report = VALIDATOR.Report()
        VALIDATOR.validate_catalog_maturity(
            "example-skill",
            status,
            {
                "structure": structure,
                "eval_spec": eval_spec,
                "forward_tested": forward_tested,
            },
            report,
        )
        return report.errors

    def test_preview_allows_pending_forward_testing(self):
        self.assertEqual(self.validate("experimental", None), [])

    def test_validated_requires_completed_forward_testing(self):
        self.assertTrue(self.validate("beta", None))
        self.assertEqual(self.validate("beta", True), [])

    def test_stable_requires_completed_forward_testing(self):
        self.assertTrue(self.validate("stable", False))
        self.assertEqual(self.validate("stable", True), [])

    def test_promotion_requires_structure_and_eval_spec(self):
        self.assertTrue(self.validate("beta", True, structure=False))
        self.assertTrue(self.validate("stable", True, eval_spec=False))

    def test_deprecated_does_not_require_forward_testing(self):
        self.assertEqual(self.validate("deprecated", None), [])


if __name__ == "__main__":
    unittest.main()
