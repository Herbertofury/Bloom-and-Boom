"""Repository routing/snapshot acceptance, not agent-behavior or gameplay proof."""
import hashlib
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
class SharedGuidanceTests(unittest.TestCase):
 def test_all_original_nonrouter_files_preserved(self):
  expected=json.loads((ROOT/'tests/guidance-preserved-files.json').read_text(encoding='utf-8'))
  self.assertEqual(len(expected),32)
  for path,digest in expected.items():
   with self.subTest(path=path):self.assertEqual(sha((ROOT/path).read_bytes()),digest)
 def test_exact_reviewed_router(self):
  self.assertEqual(sha((ROOT/'AGENTS.md').read_bytes()), '2918c05fad499c1813c9b697bbf5e4defae4c9aa9dad099dceddd97709b132ae')
  old=(ROOT/'AGENTS.md').read_text(encoding='utf-8')
  self.assertIn('Read `.agents/athena/AGENTS-adapter.md`',old)
  self.assertIn('0131c820ba311459b6f197965b8cc074512ded1a/guidance/PRODUCT_INVARIANTS.md',old)
  self.assertNotIn('.agents/foundry/',old)
  self.assertIn('Forge 47.4.23, Java 17',old)
  self.assertIn('Do not modify Enderloom/AoA',old)
 def test_pinned_athena_snapshots_complete(self):
  lock=json.loads((ROOT/'.athena/governance-lock.json').read_text(encoding='utf-8'))
  self.assertEqual(lock['sourceCommit'],'11e212bb88abd7e010c8974f35ec629032a2a843')
  self.assertEqual(lock['sourceRepository'],'https://github.com/Herbertofury/Athena')
  self.assertEqual(lock['version'],'2.0.1');self.assertIs(lock['sourceWorkingTreeDirty'],False)
  self.assertEqual(len(lock['files']),16)
  for path,digest in lock['files'].items():
   self.assertTrue(path.startswith('.agents/athena/'))
   self.assertEqual(sha((ROOT/path).read_text(encoding='utf-8').replace('\r\n','\n').encode()),digest)
  self.assertEqual((ROOT/'CLAUDE.md').read_text(encoding='utf-8'),'@AGENTS.md\n')
  self.assertTrue((ROOT/'.agents/skills/bloom-native-fidelity/SKILL.md').is_file())
if __name__=='__main__':unittest.main()
