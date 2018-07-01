import os

try:
    import cPickle as pickle # Python2
except ModuleNotFoundError:
    import pickle # Python3

from utils.visualization.lwsvm import plot as plot_svm
from utils.visualization.sgd import plot as plot_sgd
from utils.visualization.paper_plot import plot as plot_paper


def check(file_or_dir, export_pdf, show):

    assert os.path.exists(file_or_dir)

    assert export_pdf or show

    if export_pdf:
        assert isinstance(export_pdf, str) and export_pdf.endswith('.pdf')


def xp_plot(filename, export_pdf, show):

    check(filename, export_pdf, show)

    xp = pickle.load(open(filename, "rb"))

    if xp['solver'] == 'svm':
        plot_svm(filename, export_pdf, show)

    else:
        plot_sgd(filename, export_pdf, show)


def paper_plot(xp_dir, export_pdf, show):

    check(xp_dir, export_pdf, show)

    plot_paper(xp_dir, export_pdf, show)
