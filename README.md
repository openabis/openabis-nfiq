# OpenABIS NFIQ Plugin

OpenABIS' plugin for NIST Finger Image Quality (NFIQ)

##Installation

**Pipenv**
```
pipenv install git+https://github.com/openabis/openabis-nfiq.git@master#egg=openabis_nfiq

```

**Pip**
```
pip install git+https://github.com/openabis/openabis-nfiq.git@master

```

## Usage
`NFIQPlugin` requires `config` parameters that includes environment configurations:

```text
DEFAULT_FINGERPRINT_DPI (int) - fingerprint dpi, default is 0
```

