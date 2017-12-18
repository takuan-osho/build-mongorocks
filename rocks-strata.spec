Name:           rocks-strata
Version:        0.0
Release:        %(date '+%Y%m%d%H%M%s')%{?dist}
Summary:        Backup tool for mongorocks

License:        BSD
URL:            https://github.com/facebookgo/rocks-strata
# Source0:        

BuildRequires:  golang
# Requires:       

%description
rocks-strata is a framework for managing incremental backups of databases that use the RocksDB storage engine. Current drivers support MongoDB with the RocksDB storage engine ("MongoRocks") and use Amazon S3 for remote storage.

# %prep
# true
# %setup -q


%build
export GOPATH="%{_tmppath}/gopath"
mkdir -p $GOPATH
for PROJECT in github.com/facebookgo/rocks-strata/strata github.com/AdRoll/goamz/aws github.com/AdRoll/goamz/s3 github.com/AdRoll/goamz/s3/s3test github.com/facebookgo/mgotest gopkg.in/mgo.v2 gopkg.in/mgo.v2/bson golang.org/x/crypto/ssh/terminal github.com/kr/pty github.com/Azure/azure-sdk-for-go/storage github.com/minio/minio-go; do
	go get $PROJECT
done

cd $GOPATH/src/github.com/facebookgo/rocks-strata/strata/cmd/mongo/lreplica_drivers/strata
go install
cd $GOPATH/src/github.com/facebookgo/rocks-strata/strata/cmd/mongo/lreplica_drivers/mongoq
go install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}

cp $GOPATH/bin/* $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/*

%changelog


%changelog
