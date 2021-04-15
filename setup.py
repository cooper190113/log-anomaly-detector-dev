""" Setup.py for packaging log-anomaly-detector as library """
from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED_PKG = [
    "Click==7.1.2",
    "elasticsearch==5.5.6",
    "gensim==3.7.0",
    "matplotlib==3.3.4",
    "numpy==1.20.1",
    "pandas==1.0.5",
    "prometheus_client==0.9.0",
    "Flask==1.0.4",
    "scikit-learn==0.21.0",
    "scipy==1.6.2",
    "tqdm==4.59.0",
    "SQLAlchemy==1.4.3",
    "PyMySQL==1.0.2",
    "sompy",
    "boto3==1.17.48",
    "pyyaml==5.4.1",
    "numba==0.53.1",
    "kafka-python==2.0.2",
    "jaeger-client==4.4.0",
    "opentracing_instrumentation==3.3.1",
    "prometheus_flask_exporter==0.18.1",
    "gunicorn==19.9.0",
    "flask-sqlalchemy==2.5.1",
    "ipdb==0.13.0"
]

setup(
    name="log-anomaly-detector",
    version="0.0.1b5",
    py_modules=['app'],
    packages=find_packages(),
    setup_requires=["pytest-runner"],
    tests_require=[
        "pytest",
        "pytest-sugar",
        "pytest-xdist"],
    zip_safe=False,
    classifiers=(
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ),
    python_requires=">3.5",
    url="https://github.com/AICoE/log-anomaly-detector",
    author="Zak Hassan",
    author_email="zak.hassan@redhat.com",
    description="Log anomaly detector for streaming logs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    dependency_links=[
	"git+https://github.com/sevamoo/SOMPY.git@76b60ebd6ffd550b0f7faaf632451dfd68827bf7#egg=sompy",
    ],
    install_requires=REQUIRED_PKG,
    entry_points="""
        [console_scripts]
        log-anomaly-detector=app:cli
    """,
)
