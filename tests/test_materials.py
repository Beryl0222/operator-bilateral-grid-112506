"""检查合成资料的关键业务关系，避免错误输入被误作有效资料。"""
import unittest
import numpy as np
from inspect_data import load_materials

class MaterialIntegrity(unittest.TestCase):
    def test_domain_relationships(self):
        v,a=load_materials()
        h,w,c=a['source'].shape
        self.assertEqual(a['guidance'].shape,(h,w))
        self.assertEqual(a['valid'].shape,(h,w))
        self.assertEqual(a['grid'].shape,tuple(v['objects']['grid_shape']))
        self.assertTrue(((a['guidance']>=0)&(a['guidance']<=1)).all())
        for point in v['objects']['anchors']:
            x,y=point['xy'];self.assertTrue(0<=x<w and 0<=y<h)
        tiles=v['objects']['image']['tile_rects']
        self.assertEqual(tiles[0][2],tiles[1][0])

if __name__ == '__main__':
    unittest.main()
