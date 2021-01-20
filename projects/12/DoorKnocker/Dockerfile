FROM ruby:2.7.0

ENV LANG="en_US.UTF-8" LANGUAGE="en_US:UTF-8" LC_ALL="C.UTF-8"
RUN chmod a+r /etc/resolv.conf

RUN mkdir /knocker
WORKDIR /knocker
RUN gem update --system
RUN gem install bundler:2.1.4
COPY . /knocker/
RUN bundle install
CMD ["ruby", "doorknocker.rb", "-o", "0.0.0.0"]

