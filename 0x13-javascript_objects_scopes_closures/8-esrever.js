#!/usr/bin/node

exports.esrever = function (list) {
  let esrev = [];

  for (let i = list.length - 1; i >= 0; i--) {
    esrev = [...esrev, list[i]];
  }

  return esrev;
};
