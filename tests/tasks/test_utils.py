import os
from json import load

from mp_api.routes.tasks.utils import calcs_reversed_to_trajectory


def test_calcs_reversed_to_trajectory():
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, "../../test_files/calcs_reversed_mp_1031016.json")) as file:
        calcs_reversed = load(file)
        trajectories = calcs_reversed_to_trajectory(calcs_reversed)

    assert len(trajectories) == 1
    assert trajectories[0]["lattice"] == [[9.054455, 0.0, 0.0], [0.0, 4.500098, 0.0], [0.0, 0.0, 4.500098]]
