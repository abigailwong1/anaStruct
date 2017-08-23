from StructuralEngineering.FEM.system import SystemElements
from StructuralEngineering.material.profile import HEA
from StructuralEngineering.material.units import to_kNm2, to_kN


load_factor = 3

E = 210e3
profile = HEA[180]
EA = to_kN(E * profile['A'])
EI = to_kNm2(E * profile['Iy'])
mp = profile["Wy"] * 235 * 1e-6

ss = SystemElements(EA=EA, EI=EI, load_factor=load_factor)
ss.add_element([[0, 0], [0, 4]], mp={2: mp})
ss.add_element([0, 8], mp={1: mp, 2: mp})
ss.add_element([2, 8], mp={1: mp, 2: mp})
ss.add_element([4, 8], mp={1: mp, 2: mp})
ss.add_element([4, 4], mp={1: mp, 2: mp})
ss.add_element([4, 0], mp={1: mp, 2: mp})
ss.add_truss_element([[0, 4], [4, 4]])
ss.add_support_hinged(1)
ss.add_support_fixed(7)

ss.q_load(-20, 3)
ss.q_load(-20, 4)
ss.q_load(-1, 1)
ss.q_load(-1, 2)
ss.solve()

u4 = (ss.get_node_displacements(4)["uz"]**2 + ss.get_node_displacements(4)["ux"]**2)**0.5 * 1000

if __name__ == "__main__":
    print(u4)
    ss.show_structure()
    ss.show_displacement()
    ss.show_bending_moment()


