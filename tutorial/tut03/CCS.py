import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class CCS:
    """
    CCS plots Cartesian coordinate system and data.

    Example
    =======

    import numpy as np

    m1 = np.array([1, 2, 5])
    m2 = np.array([2, 3, 3])
    m3 = np.array([4, 0, 2])

    v1 = m2 - m1                # first axis
    v2 = np.cross(v1, m3 - m1)  # second axis
    v3 = np.cross(v1, v2)       # third axis

    # Vector normalization
    e1 = v1/np.linalg.norm(v1)
    e2 = v2/np.linalg.norm(v2)
    e3 = v3/np.linalg.norm(v3)

    origin = np.mean((m1, m2, m3), axis=0)
    markers = np.vstack((m1, m2, m3))
    basis = np.vstack((e1, e2, e3))

    %matplotlib notebook

    CCS(xyz=[], Oijk=origin, ijk=basis, point=markers, vector=True);

    """

    def __init__(
        self,
        ax=None,
        Oijk=[0, 0, 0],
        ijk=[],
        ijk_label=True,
        Oxyz=[0, 0, 0],
        xyz=[],
        xyz_label=True,
        point=[],
        proj_lines=True,
        vector=True,
        *args,
        **kwargs
    ):
        if not ax:
            fig = plt.figure(figsize=(5, 5))
            ax = fig.add_axes([0, 0, 1, 1], projection="3d")
        ax.axis("off")
        i0, j0, k0 = Oijk
        x0, y0, z0 = Oxyz

        if len(point):
            point = np.asarray(point)
            for xp, yp, zp in point:
                if proj_lines:
                    ax.plot3D([x0, x0], [y0, y0], [z0, zp], "k:")
                    ax.plot3D([x0, x0], [y0, yp], [z0, z0], "k:")
                    ax.plot3D([x0, x0], [y0, yp], [zp, zp], "k:")
                    ax.plot3D([x0, x0], [yp, yp], [z0, zp], "k:")
                    ax.plot3D([x0, xp], [y0, y0], [z0, z0], "k:")
                    ax.plot3D([x0, xp], [y0, y0], [zp, zp], "k:")
                    ax.plot3D([x0, xp], [yp, yp], [z0, z0], "k:")
                    ax.plot3D([x0, xp], [yp, yp], [zp, zp], "k:")
                    ax.plot3D([xp, xp], [y0, yp], [z0, z0], "k:")
                    ax.plot3D([xp, xp], [y0, yp], [zp, zp], "k:")
                    ax.plot3D([xp, xp], [y0, y0], [z0, zp], "k:")
                    ax.plot3D([xp, xp], [yp, yp], [z0, zp], "k:")

        xmin, xmax, ymin, ymax, zmin, zmax = ax.get_w_lims()
        xr = 0.1 * (xmax - xmin)
        yr = 0.1 * (ymax - ymin)
        zr = 0.1 * (zmax - zmin)
        xyzmin = np.min((xmin - xr, ymin - yr, zmin - zr))
        xyzmax = np.max((xmax + xr, ymax + yr, zmax + zr))
        ax.set_xlim3d(xyzmin, xyzmax)
        ax.set_ylim3d(xyzmin, xyzmax)
        ax.set_zlim3d(xyzmin, xyzmax)

        if not len(xyz):
            xyz = np.max((xmax, ymax, zmax))
            xyz = [[xyz, 0, 0], [0, xyz, 0], [0, 0, xyz]]
        if len(xyz):
            xyz = np.asarray(xyz)
            x, y, z = xyz
            xa = Arrow3D(
                [x0, x0 + x[0]],
                [y0, y0 + x[1]],
                [z0, z0 + x[2]],
                mutation_scale=20,
                lw=2,
                arrowstyle="->",
                color="k",
                alpha=0.8,
            )
            ya = Arrow3D(
                [x0, x0 + y[0]],
                [y0, y0 + y[1]],
                [z0, z0 + y[2]],
                mutation_scale=20,
                lw=2,
                arrowstyle="->",
                color="k",
                alpha=0.8,
            )
            za = Arrow3D(
                [x0, x0 + z[0]],
                [y0, y0 + z[1]],
                [z0, z0 + z[2]],
                mutation_scale=20,
                lw=2,
                arrowstyle="->",
                color="k",
                alpha=0.8,
            )
            ax.add_artist(xa)
            ax.add_artist(ya)
            ax.add_artist(za)
            if xyz_label:
                ax.text(x0 + xyzmax, y0, z0, "X", fontsize=20, color="black")
                ax.text(x0, y0 + xyzmax, z0, "Y", fontsize=20, color="black")
                ax.text(x0, y0, z0 + xyzmax, "Z", fontsize=20, color="black")

        if not len(ijk):
            ijk = np.min((xmax, ymax, zmax)) / 2
            ijk = [[ijk, 0, 0], [0, ijk, 0], [0, 0, ijk]]
        if len(ijk):
            ijk = np.asarray(ijk)
            i, j, k = ijk
            ia = Arrow3D(
                [i0, i0 + i[0]],
                [j0, j0 + i[1]],
                [k0, k0 + i[2]],
                mutation_scale=10,
                lw=3,
                arrowstyle="-|>",
                color="r",
                alpha=0.8,
            )
            ja = Arrow3D(
                [i0, i0 + j[0]],
                [j0, j0 + j[1]],
                [k0, k0 + j[2]],
                mutation_scale=10,
                lw=3,
                arrowstyle="-|>",
                color="g",
                alpha=0.8,
            )
            ka = Arrow3D(
                [i0, i0 + k[0]],
                [j0, j0 + k[1]],
                [k0, k0 + k[2]],
                mutation_scale=10,
                lw=3,
                arrowstyle="-|>",
                color="b",
                alpha=0.8,
            )
            ax.add_artist(ia)
            ax.add_artist(ja)
            ax.add_artist(ka)
            if ijk_label:
                ax.text(
                    i0 + i[0],
                    j0 + i[1],
                    k0 + i[2],
                    "i",
                    fontsize=20,
                    color="red",
                )
                ax.text(
                    i0 + j[0],
                    j0 + j[1],
                    k0 + j[2],
                    "j",
                    fontsize=20,
                    color="green",
                )
                ax.text(
                    i0 + k[0],
                    j0 + k[1],
                    k0 + k[2],
                    "k",
                    fontsize=20,
                    color="blue",
                )

        if len(point):
            point = np.asarray(point)
            for xp, yp, zp in point:
                ax.plot3D(
                    [xp], [yp], [zp], marker="o", color="y", alpha=0.8, ms=8
                )
                if vector:
                    v = Arrow3D(
                        [x0, xp],
                        [y0, yp],
                        [z0, zp],
                        mutation_scale=15,
                        lw=3,
                        arrowstyle="-|>",
                        color="y",
                        alpha=0.8,
                    )
                    ax.add_artist(v)

        ax.view_init(elev=20, azim=60)
        plt.show()


class Arrow3D(FancyArrowPatch):
    """See https://github.com/matplotlib/matplotlib/issues/21688#issuecomment-974912574"""

    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)
